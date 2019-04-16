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
	mov $4,%ecx
	mov %ecx, -4(%ebp)
	mov -4(%ebp),%ebx
	add $6,%ebx
	mov %ebx, -8(%ebp)
	mov -8(%ebp),%ebx
	sub $2,%ebx
	mov %ebx, -12(%ebp)
	mov -12(%ebp),%ebx
	add $7,%ebx
	mov %ebx, -16(%ebp)
	mov -16(%ebp),%ebx
	sub $3,%ebx
	mov %ebx, -20(%ebp)
	mov -20(%ebp),%ebx
	add $8,%ebx
	mov %ebx, -24(%ebp)
	mov -24(%ebp),%ebx
	add $9,%ebx
	mov %ebx, -28(%ebp)
	mov -28(%ebp),%ebx
	add $10,%ebx
	mov %ebx, -32(%ebp)
	mov -32(%ebp),%ebx
	add $5,%ebx
	mov %ebx, -36(%ebp)
	mov -36(%ebp),%ebx
	sub $1,%ebx
	mov %ebx, -40(%ebp)
	mov -40(%ebp),%ebx
	add $6,%ebx
	mov %ebx, -44(%ebp)
	mov -44(%ebp),%ebx
	sub $2,%ebx
	mov %ebx, -48(%ebp)
	mov -48(%ebp),%ebx
	add $7,%ebx
	mov %ebx, -52(%ebp)
	mov -52(%ebp),%ebx
	sub $3,%ebx
	mov %ebx, -56(%ebp)
	mov -56(%ebp),%ebx
	add $8,%ebx
	mov %ebx, -60(%ebp)
	mov -60(%ebp),%ebx
	add $9,%ebx
	mov %ebx, -64(%ebp)
	mov -64(%ebp),%ebx
	add $10,%ebx
	mov %ebx, -68(%ebp)
	mov -68(%ebp),%ebx
	add $5,%ebx
	mov %ebx, -72(%ebp)
	mov -72(%ebp),%ebx
	sub $1,%ebx
	mov %ebx, -76(%ebp)
	mov -76(%ebp),%ebx
	add $6,%ebx
	mov %ebx, -80(%ebp)
	mov -80(%ebp),%ebx
	sub $2,%ebx
	mov %ebx, -84(%ebp)
	mov -84(%ebp),%ebx
	add $7,%ebx
	mov %ebx, -88(%ebp)
	mov -88(%ebp),%ebx
	sub $3,%ebx
	mov %ebx, -92(%ebp)
	mov -92(%ebp),%ebx
	add $8,%ebx
	mov %ebx, -96(%ebp)
	mov -96(%ebp),%ebx
	add $9,%ebx
	mov %ebx, -100(%ebp)
	mov -100(%ebp),%ebx
	add $10,%ebx
	mov %ebx, -104(%ebp)
	mov -104(%ebp), %eax
	mov %eax, -108(%ebp)
	push -108(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov $1, %eax
	int $0x80
