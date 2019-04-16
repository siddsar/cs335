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
	mov $42, %eax
	mov %eax, -4(%ebp)
	push -4(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov -4(%ebp),%ebx
	add $5,%ebx
	mov %ebx, -8(%ebp)
	push -8(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov $1, %eax
	int $0x80
