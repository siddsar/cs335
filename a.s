	.data
	outFormatInt:
	.string "%d\n"
	outFormatStr:
	.string "%s\n"
	inFormat:
	.string "%d\n"
	.global main
fact:
	push %ebp
	mov %esp, %ebp
	add $-512, %esp
	mov 8(%ebp), %eax
	mov %eax, -4(%ebp)
	mov -4(%ebp), %eax
	mov $1, %ebx
	cmp %ebx, %eax
	je scope2
scope1:
	mov $0, %eax
	mov %eax, -8(%ebp)
	jmp scope3
scope2:
	mov $1, %eax
	mov %eax, -8(%ebp)
scope3:
	mov -8(%ebp), %eax
	mov $0, %ebx
	cmp %ebx, %eax
	je scope5
	jmp scope4
scope4:
	mov $1, %eax
	mov %ebp, %esp
	pop %ebp
	ret
scope5:
	mov -4(%ebp),%ebx
	sub $1,%ebx
	mov %ebx, -12(%ebp)
	push -12(%ebp)
	call fact
	mov %eax, -16(%ebp)
	add $4, %esp
	mov -4(%ebp),%eax
	imul -16(%ebp),%eax
	mov %eax,-20(%ebp)
	mov -20(%ebp), %eax
	mov %ebp, %esp
	pop %ebp
	ret
	mov %ebp, %esp
	pop %ebp
	ret
main:
	push %ebp
	mov %esp, %ebp
	add $-512, %esp
	push $6
	call fact
	mov %eax, -4(%ebp)
	add $4, %esp
	mov -4(%ebp), %eax
	mov %eax, -8(%ebp)
	push -8(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov $1, %eax
	int $0x80
