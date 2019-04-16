	.data
	outFormatInt:
	.string "%d\n"
	outFormatStr:
	.string "%s\n"
	inFormat:
	.string "%d\n"
	.global main
main:
	push %ebp
	mov %esp, %ebp
	add $-512, %esp
	mov $1, %eax
	mov %eax, -16(%ebp)
	mov -16(%ebp),%ebx
	imul $2,%ebx
	mov %ebx, -16(%ebp)
	mov -16(%ebp),%ebx
	imul $2,%ebx
	mov %ebx, -16(%ebp)
	mov $0, %eax
	mov %eax, -36(%ebp)
	mov -36(%ebp),%ebx
	imul $2,%ebx
	mov %ebx, -36(%ebp)
	mov -36(%ebp),%ebx
	add $0,%ebx
	mov %ebx, -36(%ebp)
	mov -36(%ebp), %eax
	add -32(%ebp), %eax
	mov -40(%ebp), %ebx
	mov (%eax), %ebx
	mov -36(%ebp), %eax
	add -32(%ebp), %eax
	mov 1, %ebx
	mov %ebx, (%eax)
	mov $0, %eax
	mov %eax, -44(%ebp)
	mov -44(%ebp),%ebx
	imul $2,%ebx
	mov %ebx, -44(%ebp)
	mov -44(%ebp),%ebx
	add $1,%ebx
	mov %ebx, -44(%ebp)
	mov -44(%ebp), %eax
	add -32(%ebp), %eax
	mov -48(%ebp), %ebx
	mov (%eax), %ebx
	mov -44(%ebp), %eax
	add -32(%ebp), %eax
	mov 2, %ebx
	mov %ebx, (%eax)
	mov $1, %eax
	mov %eax, -52(%ebp)
	mov -52(%ebp),%ebx
	imul $2,%ebx
	mov %ebx, -52(%ebp)
	mov -52(%ebp),%ebx
	add $0,%ebx
	mov %ebx, -52(%ebp)
	mov -52(%ebp), %eax
	add -32(%ebp), %eax
	mov -56(%ebp), %ebx
	mov (%eax), %ebx
	mov -52(%ebp), %eax
	add -32(%ebp), %eax
	mov 3, %ebx
	mov %ebx, (%eax)
	mov $1, %eax
	mov %eax, -60(%ebp)
	mov -60(%ebp),%ebx
	imul $2,%ebx
	mov %ebx, -60(%ebp)
	mov -60(%ebp),%ebx
	add $1,%ebx
	mov %ebx, -60(%ebp)
	mov -60(%ebp), %eax
	add -32(%ebp), %eax
	mov -64(%ebp), %ebx
	mov (%eax), %ebx
	mov -60(%ebp), %eax
	add -32(%ebp), %eax
	mov 4, %ebx
	mov %ebx, (%eax)
	mov $1, %eax
	int $0x80
