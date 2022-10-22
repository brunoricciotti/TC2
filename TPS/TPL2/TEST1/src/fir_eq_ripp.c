/*
===============================================================================
 Name        : fir_eq_rip.c
 Author      : $(author)
 Version     :
 Copyright   : $(copyright)
 Description : main definition
===============================================================================
*/

#ifdef __USE_CMSIS
#include "LPC17xx.h"
#endif

#include <cr_section_macros.h>

/* ----------------------------------------------------------------------
** Include Files
** ------------------------------------------------------------------- */

#include "arm_math.h"
#include "math_helper.h"

#if defined(SEMIHOSTING)
#include <stdio.h>
#endif

#include "dsp/filtering_functions.h"
#include "dsp/support_functions.h"
/* ----------------------------------------------------------------------
** Macro Defines
** ------------------------------------------------------------------- */

#define TEST_LENGTH_SAMPLES  320
/*

This SNR is a bit small. Need to understand why
this example is not giving better SNR ...

*/
#define SNR_THRESHOLD_F32    75.0f
#define BLOCK_SIZE            32

#if defined(ARM_MATH_MVEF) && !defined(ARM_MATH_AUTOVECTORIZE)
/* Must be a multiple of 16 */
#define NUM_TAPS_ARRAY_SIZE              32
#else
#define NUM_TAPS_ARRAY_SIZE              32
#endif

#define NUM_TAPS              32

/* -------------------------------------------------------------------
 * The input signal and reference output (computed with MATLAB)
 * are defined externally in arm_fir_lpf_data.c.
 * ------------------------------------------------------------------- */

extern float32_t testInput_f32_1kHz_15kHz[TEST_LENGTH_SAMPLES];
extern float32_t refOutput[TEST_LENGTH_SAMPLES];

/* -------------------------------------------------------------------
 * Declare Test output buffer
 * ------------------------------------------------------------------- */

static q31_t testOutput[TEST_LENGTH_SAMPLES];

/* -------------------------------------------------------------------
 * Declare State buffer of size (numTaps + blockSize - 1)
 * ------------------------------------------------------------------- */
#if defined(ARM_MATH_MVEF) && !defined(ARM_MATH_AUTOVECTORIZE)
static float32_t firStateF32[2 * BLOCK_SIZE + NUM_TAPS - 1];
#else
static q31_t firStateQ31[BLOCK_SIZE + NUM_TAPS - 1];
#endif

/* ----------------------------------------------------------------------
** FIR Coefficients buffer generated using fir1() MATLAB function.
** fir1(28, 6/24)
** ------------------------------------------------------------------- */
#if defined(ARM_MATH_MVEF) && !defined(ARM_MATH_AUTOVECTORIZE)
const float32_t firCoeffs32[NUM_TAPS_ARRAY_SIZE] = {
  -0.0018225230f, -0.0015879294f, +0.0000000000f, +0.0036977508f, +0.0080754303f, +0.0085302217f, -0.0000000000f, -0.0173976984f,
  -0.0341458607f, -0.0333591565f, +0.0000000000f, +0.0676308395f, +0.1522061835f, +0.2229246956f, +0.2504960933f, +0.2229246956f,
  +0.1522061835f, +0.0676308395f, +0.0000000000f, -0.0333591565f, -0.0341458607f, -0.0173976984f, -0.0000000000f, +0.0085302217f,
  +0.0080754303f, +0.0036977508f, +0.0000000000f, -0.0015879294f, -0.0018225230f, 0.0f,0.0f,0.0f
};
#else
//const float32_t firCoeffs32[NUM_TAPS_ARRAY_SIZE] = {
//  -0.0018225230f, -0.0015879294f, +0.0000000000f, +0.0036977508f, +0.0080754303f, +0.0085302217f, -0.0000000000f, -0.0173976984f,
//  -0.0341458607f, -0.0333591565f, +0.0000000000f, +0.0676308395f, +0.1522061835f, +0.2229246956f, +0.2504960933f, +0.2229246956f,
//  +0.1522061835f, +0.0676308395f, +0.0000000000f, -0.0333591565f, -0.0341458607f, -0.0173976984f, -0.0000000000f, +0.0085302217f,
//  +0.0080754303f, +0.0036977508f, +0.0000000000f, -0.0015879294f, -0.0018225230f
//};
const float32_t firCoeffs32[NUM_TAPS_ARRAY_SIZE] = {
	0.010405,0.007894,0.010593,0.013653,0.017030,0.020651,0.024432,0.028284,
	0.032103,0.035769,0.039171,0.042209,0.044763,0.046766,0.048137,0.048837,
	0.048837,0.048137,0.046766,0.044763,0.042209,0.039171,0.035769,0.032103,
	0.028284,0.024432,0.020651,0.017030,0.013653,0.010593,0.007894,0.010405
};
#endif

q31_t firCoeffsQ31[NUM_TAPS_ARRAY_SIZE];

/* ------------------------------------------------------------------
 * Global variables for FIR LPF Example
 * ------------------------------------------------------------------- */

uint32_t blockSize = BLOCK_SIZE;
uint32_t numBlocks = TEST_LENGTH_SAMPLES/BLOCK_SIZE;

float32_t  snr;

/* ----------------------------------------------------------------------
 * FIR LPF Example
 * ------------------------------------------------------------------- */

int32_t main(void)
{
  uint32_t i;
  arm_fir_instance_q31 S;
  //arm_status status;
  q31_t  *inputQ31, *outputQ31;
  q31_t testInput_q31_1kHz_15kHz[TEST_LENGTH_SAMPLES];
  float32_t testOutput_f32[TEST_LENGTH_SAMPLES];

  /* Initialize input and output buffer pointers */
  inputQ31 = &testInput_q31_1kHz_15kHz[0];
  outputQ31 = &testOutput[0];

  arm_float_to_q31(firCoeffs32,firCoeffsQ31,blockSize);
  arm_float_to_q31(testInput_f32_1kHz_15kHz,testInput_q31_1kHz_15kHz,TEST_LENGTH_SAMPLES);

  /* Call FIR init function to initialize the instance structure. */
  arm_fir_init_q31(&S, NUM_TAPS, (q31_t *)&firCoeffsQ31[0], &firStateQ31[0], blockSize);

  /* ----------------------------------------------------------------------
  ** Call the FIR process function for every blockSize samples
  ** ------------------------------------------------------------------- */

  for(i=0; i < numBlocks; i++)
  {
    arm_fir_q31(&S, inputQ31 + (i * blockSize), outputQ31 + (i * blockSize), blockSize);
  }

  /* ----------------------------------------------------------------------
  ** Compare the generated output against the reference output computed
  ** in MATLAB.
  ** ------------------------------------------------------------------- */
  arm_q31_to_float(testOutput,testOutput_f32,TEST_LENGTH_SAMPLES);
  //snr = arm_snr_f32(&refOutput[0], &testOutput[0], TEST_LENGTH_SAMPLES);

  //status = (snr < SNR_THRESHOLD_F32) ? ARM_MATH_TEST_FAILURE : ARM_MATH_SUCCESS;
  while (1);

//  if (status != ARM_MATH_SUCCESS)
//  {
//#if defined (SEMIHOSTING)
//    printf("FAILURE\n");
//#else
//    while (1);                             /* main function does not return */
//#endif
//  }
//  else
//  {
//#if defined (SEMIHOSTING)
//    printf("SUCCESS\n");
//#else
//    while (1);                             /* main function does not return */
//#endif
//  }
}

/** \endlink */
