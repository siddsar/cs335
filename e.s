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
	mov $0, %eax
	mov %eax, -16(%ebp)
	mov -16(%ebp), %eax
	imul $4, %eax
	add %ebp, %eax
	add $-12, %eax
	mov (%eax), %ebx
	mov %ebx, -20(%ebp)
	mov -16(%ebp), %eax
	imul $4, %eax
	add %ebp, %eax
	add $-12, %eax
	mov $100, %ebx
	mov %ebx, (%eax)
	mov $1, %eax
	mov %eax, -24(%ebp)
	mov -24(%ebp), %eax
	imul $4, %eax
	add %ebp, %eax
	add $-12, %eax
	mov (%eax), %ebx
	mov %ebx, -28(%ebp)
	mov -24(%ebp), %eax
	imul $4, %eax
	add %ebp, %eax
	add $-12, %eax
	mov $200, %ebx
	mov %ebx, (%eax)
	mov $0, %eax
	mov %eax, -32(%ebp)
	mov -32(%ebp), %eax
	imul $4, %eax
	add %ebp, %eax
	add $-12, %eax
	mov (%eax), %ebx
	mov %ebx, -36(%ebp)
	push -36(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov $1, %eax
	mov %eax, -40(%ebp)
	mov -40(%ebp), %eax
	imul $4, %eax
	add %ebp, %eax
	add $-12, %eax
	mov (%eax), %ebx
	mov %ebx, -44(%ebp)
	push -44(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov $1, %eax
	int $0x80
