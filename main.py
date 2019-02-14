from timeit import default_timer  # Timer to keep track of runtime for each function


# ===========================================================
# PROBLEM 1 -- Multiples of 3 and 5
# ===========================================================
#
# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6, and 9. The sum of
# these multiples is 23.
#
# Find the sum of all multiples of 3 or 5 below 1000
#
# ===========================================================

# Method A:  1000 iterations
# Description:
#   iterate through all integers 0-999, and add it to the sum
#   if it is divisible by three or five
# Note:
#   Only calculation is timed, not result output
def problem_1_method_a( maximum=1000 ):
    # Print Problem Context
    print( "Project Euler Problem 1 -- Method 1 (1000 Iterations)" )

    # Prepare Variables
    start_time  =  default_timer( )  # Timer Start
    result      =  0                 # Result

    # Iterate
    for x in range( maximum ):
        # Conditions: 3 or 5 evenly divide the number
        if x % 3 is 0 or x % 5 is 0:
            result  +=  x

    # Compute Runtime
    end_time        =  default_timer( )                  # Timer End
    execution_time  =  ( end_time - start_time ) * 1000  # Total Execution Time

    # Output the Result and the Time to calculate result
    print( "   Sum of all multiples of 3 or 5 below 1000:   %d"        %  result )
    print( "   Calculation Time:                            %.3fms\n"  %  execution_time )
    return



# Method B:  598 iterations
# Description:
#   1. iterate through all multiples of 3 <1000 and add to result
#   2. iterate through all multiples of 5 <1000 and add to result
#   3. the LCM of 3 and 5 is 15, so exclude multiples of 15 in
#      step 2 (to prevent double-counting those values)
# Note:
#   Only calculation is timed, not result output
def problem_1_method_b( maximum=1000 ):
    # Print Problem Context (unnecessary)
    print( "Project Euler Problem 1 -- Method 2 (598 Iterations)" )

    # Prepare Variables
    start_time  =  default_timer( )
    result      =  0

    # Sum the multiples of 3
    for x in range( 3 , maximum , 3 ):
        result  +=  x

    # Sum the multiples of 5
    for x in range( 5 , maximum , 5 ):
        # Exclude the LCM (already appeared in multiples of 3)
        if x % 15 == 0:
            continue
        result  +=  x

    # Compute Runtime
    end_time        =  default_timer( )  # Timer End
    execution_time  =  ( end_time - start_time ) * 1000  # Total Execution Time

    # Output the Result and the Time to calculate result
    print( "   Sum of all multiples of 3 or 5 below 1000:   %d"        %  result )
    print( "   Calculation Time:                            %.3fms\n"  %  execution_time )
    return



# Use of generator instead of looping
def problem_1_method_c( maximum=1000 ):
    # Print Problem Context (unnecessary)
    print("Project Euler Problem 1 -- Method 3 (Generator Function)")

    # Prepare Variables
    start_time  =  default_timer( )
    result      =  sum( [ x for x in range( 1 , maximum )
                            if x % 3 == 0
                            or x % 5 == 0 ] )

    # Compute Runtime
    end_time        =  default_timer( )                  # Timer End
    execution_time  =  ( end_time - start_time ) * 1000  # Total Execution Time

    print( "   Sum of all multiples of 3 or 5 below 1000:   %d"        %  result )
    print( "   Calculation Time:                            %.3fms\n"  %  execution_time )
    return



def main( ):
    problem_1_method_a( )
    problem_1_method_b( )
    problem_1_method_c( )



if __name__  ==  '__main__':
    main( )
