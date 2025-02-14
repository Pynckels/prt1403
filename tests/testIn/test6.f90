program performance_test
    implicit none
    integer :: i, total
    real(8) :: start_time, end_time

    total = 0
    call cpu_time(start_time)

    do i = 1, 10000000
        total = total + i
    end do

    call cpu_time(end_time)

    print *, "Fortran: The sum is ", total
    print *, "Fortran: Time taken = ", end_time - start_time
end program performance_test
