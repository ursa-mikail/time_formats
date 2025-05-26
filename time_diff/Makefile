# for time_diff.cu and time_diff.c

# Makefile for C and CUDA timing examples
# Compiler for C
CC = gcc
CFLAGS = -O2 -Wall

# Compiler for CUDA
NVCC = nvcc
NVFLAGS = -O2

# Targets
TARGETS = time_diff_c time_diff_cuda

# Rules
all: $(TARGETS)

# Compile C version
time_diff_c: time_diff.c
	$(CC) $(CFLAGS) -o $@ $^

# Compile CUDA version
time_diff_cuda: time_diff.cu
	$(NVCC) $(NVFLAGS) -o $@ $^

# Clean
clean:
	rm -f $(TARGETS)

#make          # Builds both time_diff_c and time_diff_cuda
#./time_diff_c
#./time_diff_cuda
#make clean    # Cleans up binaries