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
	add $512, %esp
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
	push $25
	push $outFormatInt
	call printf
	add $8, %esp
	push -4(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov $1, %eax
	mov %ebp, %esp
	pop %ebp
	ret
scope5:
	push -4(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov -4(%ebp),%ebx
	sub $1,%ebx
	mov %ebx, -12(%ebp)
	mov -12(%ebp), %eax
	mov %eax, -16(%ebp)
	push -16(%ebp)
	call fact
	mov %eax, -20(%ebp)
	add $4, %esp
	mov -20(%ebp), %eax
	mov %eax, -24(%ebp)
	push -24(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	push -4(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov -4(%ebp),%eax
	imul -24(%ebp),%eax
	mov %eax,-28(%ebp)
	mov -28(%ebp), %eax
	mov %ebp, %esp
	pop %ebp
	ret
	mov %ebp, %esp
	pop %ebp
	ret
main:
	push %ebp
	mov %esp, %ebp
	add $512, %esp
	mov $325, %eax
	mov %eax, -4(%ebp)
	push -4(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	push $25
	push $outFormatInt
	call printf
	add $8, %esp
	push -4(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov $25, %eax
	mov %eax, -8(%ebp)
	mov $0, %eax
	mov %eax, -12(%ebp)
scope7:
	mov -12(%ebp), %eax
	mov $8, %ebx
	cmp %ebx, %eax
	jl scope12
scope11:
	mov $0, %eax
	mov %eax, -16(%ebp)
	jmp scope13
scope12:
	mov $1, %eax
	mov %eax, -16(%ebp)
scope13:
	jmp scope8
scope9:
	mov -12(%ebp),%ebx
	add $1,%ebx
	mov %ebx, -20(%ebp)
	mov -20(%ebp), %eax
	mov %eax, -12(%ebp)
	jmp scope7
scope8:
	mov -16(%ebp), %eax
	mov $0, %ebx
	cmp %ebx, %eax
	je scope10
	mov -8(%ebp),%ebx
	add $13,%ebx
	mov %ebx, -24(%ebp)
	mov -24(%ebp), %eax
	mov %eax, -8(%ebp)
	push $15
	push $outFormatInt
	call printf
	add $8, %esp
	push -8(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	jmp scope9
scope10:
	mov $1, %eax
	int $0x80
