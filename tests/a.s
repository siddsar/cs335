	.data
	outFormatInt:
	.string "%d\n"
	outFormatStr:
	.string "%s\n"
	inFormat:
	.string "%d\n"
	.global main
ackermann:
	push %ebp
	mov %esp, %ebp
	add $-512, %esp
	mov 8(%ebp), %eax
	mov %eax, -4(%ebp)
	mov 12(%ebp), %eax
	mov %eax, -8(%ebp)
	mov $-1, %eax
	mov %eax, -12(%ebp)
	mov $-1, %eax
	mov %eax, -16(%ebp)
	push -4(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	push -8(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov -4(%ebp), %eax
	mov $-1, %ebx
	cmp %ebx, %eax
	jg scope2
scope1:
	mov $0, %eax
	mov %eax, -20(%ebp)
	jmp scope3
scope2:
	mov $1, %eax
	mov %eax, -20(%ebp)
scope3:
	mov -8(%ebp), %eax
	mov $-1, %ebx
	cmp %ebx, %eax
	jg scope5
scope4:
	mov $0, %eax
	mov %eax, -24(%ebp)
	jmp scope6
scope5:
	mov $1, %eax
	mov %eax, -24(%ebp)
scope6:
	mov -20(%ebp), %eax
	mov %eax, -28(%ebp)
	mov -20(%ebp), %eax
	mov $0, %ebx
	cmp %ebx, %eax
	je scope7
	mov -20(%ebp),%ebx
	mov -24(%ebp),%eax
	and %ebx,%eax
	mov %ebx, -28(%ebp)
scope7:
	mov -28(%ebp), %eax
	mov $0, %ebx
	cmp %ebx, %eax
	je scope9
	jmp scope8
scope8:
	mov -4(%ebp), %eax
	mov $0, %ebx
	cmp %ebx, %eax
	je scope11
scope10:
	mov $0, %eax
	mov %eax, -32(%ebp)
	jmp scope12
scope11:
	mov $1, %eax
	mov %eax, -32(%ebp)
scope12:
	mov -32(%ebp), %eax
	mov $0, %ebx
	cmp %ebx, %eax
	je scope14
	jmp scope13
scope13:
	mov -8(%ebp),%ebx
	add $1,%ebx
	mov %ebx, -36(%ebp)
	mov -36(%ebp), %eax
	mov %eax, -12(%ebp)
	jmp scope15
scope14:
	mov -8(%ebp), %eax
	mov $0, %ebx
	cmp %ebx, %eax
	je scope17
scope16:
	mov $0, %eax
	mov %eax, -40(%ebp)
	jmp scope18
scope17:
	mov $1, %eax
	mov %eax, -40(%ebp)
scope18:
	mov -40(%ebp), %eax
	mov $0, %ebx
	cmp %ebx, %eax
	je scope20
	jmp scope19
scope19:
	mov -4(%ebp),%ebx
	sub $1,%ebx
	mov %ebx, -44(%ebp)
	push $1
	push -44(%ebp)
	call ackermann
	mov %eax, -48(%ebp)
	add $8, %esp
	mov -48(%ebp), %eax
	mov %eax, -12(%ebp)
	jmp scope21
scope20:
	mov -8(%ebp),%ebx
	sub $1,%ebx
	mov %ebx, -52(%ebp)
	push -52(%ebp)
	push -4(%ebp)
	call ackermann
	mov %eax, -56(%ebp)
	add $8, %esp
	mov -56(%ebp), %eax
	mov %eax, -16(%ebp)
	mov -4(%ebp),%ebx
	sub $1,%ebx
	mov %ebx, -60(%ebp)
	push -16(%ebp)
	push -60(%ebp)
	call ackermann
	mov %eax, -64(%ebp)
	add $8, %esp
	mov -64(%ebp), %eax
	mov %eax, -12(%ebp)
scope21:
scope15:
scope9:
	mov -12(%ebp), %eax
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
	push $1
	push $3
	call ackermann
	mov %eax, -4(%ebp)
	add $8, %esp
	mov -4(%ebp), %eax
	mov %eax, -8(%ebp)
	push -8(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov $1, %eax
	int $0x80
	