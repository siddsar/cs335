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
	mov $6, %eax
	mov %eax, -4(%ebp)
	push -4(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	lea -4(%ebp), %eax
	push %eax
	push $inFormat
	call scanf
	add $8, %esp
	push -4(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov $1, %eax
	int $0x80
