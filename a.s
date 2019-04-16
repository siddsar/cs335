	.data
	outFormatInt:
	.string "%d\n"
	outFormatStr:
	.string "%s\n"
	inFormat:
	.string "%d\n"
	.global main
odd_function:
	push %ebp
	mov %esp, %ebp
	add $-512, %esp
	mov 8(%ebp), %eax
	mov %eax, -4(%ebp)
	push $-1
	push $outFormatInt
	call printf
	add $8, %esp
	push -4(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov -4(%ebp), %eax
	mov $0, %ebx
	cmp %ebx, %eax
	je scope2
scope1:
	mov $0, %eax
	mov %eax, -12(%ebp)
	jmp scope3
scope2:
	mov $1, %eax
	mov %eax, -12(%ebp)
scope3:
	mov -12(%ebp), %eax
	mov $0, %ebx
	cmp %ebx, %eax
	je scope5
	jmp scope4
scope4:
	mov $0, %eax
	mov %eax, -8(%ebp)
	jmp scope6
scope5:
	mov -4(%ebp),%ebx
	sub $1,%ebx
	mov %ebx, -16(%ebp)
