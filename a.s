.data
	outFormatInt:
	.string "%d\n"
	outFormatStr:
	.string "%s\n"
	inFormat:
	.string "%d\n"
	.global main
<<<<<<< HEAD
['func', 'main', '', '']
main:
	push %ebp
	mov %esp, %ebp
	add $-512, %esp
['kaizoku_2', '0', '', '=']
	mov $0, %eax
	mov %eax, -16(%ebp)
['kaizoku_3', 'a', 'kaizoku_2', '=arr']
	mov -16(%ebp), %eax
	add %ebp, %eax
	add $-12, %eax
	mov (%eax), %ebx
	mov %ebx, -20(%ebp)
['a', 'kaizoku_2', '0', 'arr=']
	mov -16(%ebp), %eax
	add %ebp, %eax
	add $-12, %eax
	mov $0, %ebx
	mov %ebx, (%eax)
['kaizoku_4', '1', '', '=']
	mov $1, %eax
	mov %eax, -24(%ebp)
['kaizoku_5', 'a', 'kaizoku_4', '=arr']
	mov -24(%ebp), %eax
	add %ebp, %eax
	add $-12, %eax
	mov (%eax), %ebx
	mov %ebx, -28(%ebp)
['a', 'kaizoku_4', '0', 'arr=']
	mov -24(%ebp), %eax
	add %ebp, %eax
	add $-12, %eax
	mov $0, %ebx
	mov %ebx, (%eax)
['kaizoku_6', '0', '', '=']
	mov $0, %eax
	mov %eax, -32(%ebp)
['kaizoku_7', 'a', 'kaizoku_6', '=arr']
	mov -32(%ebp), %eax
	add %ebp, %eax
	add $-12, %eax
	mov (%eax), %ebx
	mov %ebx, -36(%ebp)
['print', 'kaizoku_7', '', '_INT']
	push -36(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
['kaizoku_8', '1', '', '=']
	mov $1, %eax
	mov %eax, -40(%ebp)
['kaizoku_9', 'a', 'kaizoku_8', '=arr']
	mov -40(%ebp), %eax
	add %ebp, %eax
	add $-12, %eax
	mov (%eax), %ebx
	mov %ebx, -44(%ebp)
['print', 'kaizoku_9', '', '_INT']
	push -44(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
['ret', '', 'main', '']
	mov $1, %eax
	int $0x80
=======
odd_function:
	push %ebp
	mov %esp, %ebp
	add $-512, %esp
<<<<<<< HEAD
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
=======
	mov $0, %eax
	mov %eax, -28(%ebp)
	mov -28(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov (%eax), %ebx
	mov %ebx, -32(%ebp)
	mov -28(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov $84, %ebx
	mov %ebx, (%eax)
	mov $1, %eax
	mov %eax, -36(%ebp)
	mov -36(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov (%eax), %ebx
	mov %ebx, -40(%ebp)
	mov -36(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov $14, %ebx
	mov %ebx, (%eax)
	mov $2, %eax
	mov %eax, -44(%ebp)
	mov -44(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov (%eax), %ebx
	mov %ebx, -48(%ebp)
	mov -44(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov $832354, %ebx
	mov %ebx, (%eax)
	mov $3, %eax
	mov %eax, -52(%ebp)
	mov -52(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov (%eax), %ebx
	mov %ebx, -56(%ebp)
	mov -52(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov $12254, %ebx
	mov %ebx, (%eax)
	mov $4, %eax
	mov %eax, -60(%ebp)
	mov -60(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov (%eax), %ebx
	mov %ebx, -64(%ebp)
	mov -60(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov $348687, %ebx
	mov %ebx, (%eax)
	mov $0, %eax
	mov %eax, -68(%ebp)
	mov -68(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov (%eax), %ebx
	mov %ebx, -72(%ebp)
	push -72(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	mov $0, %eax
	mov %eax, -72(%ebp)
scope2:
	mov -72(%ebp), %eax
	mov $5, %ebx
	cmp %ebx, %eax
	jl scope7
scope6:
	mov $0, %eax
	mov %eax, -76(%ebp)
	jmp scope8
scope7:
	mov $1, %eax
	mov %eax, -76(%ebp)
scope8:
	jmp scope3
scope4:
	mov -72(%ebp),%ebx
	add $1,%ebx
	mov %ebx, -72(%ebp)
	jmp scope2
scope3:
	mov -76(%ebp), %eax
	mov $0, %ebx
	cmp %ebx, %eax
	je scope5
	mov -72(%ebp), %eax
	mov %eax, -80(%ebp)
	mov -80(%ebp), %eax
	add %ebp, %eax
	add $-24, %eax
	mov (%eax), %ebx
	mov %ebx, -84(%ebp)
	push -84(%ebp)
	push $outFormatInt
	call printf
	add $8, %esp
	jmp scope4
scope5:
	mov $1, %eax
	int $0x80
>>>>>>> 8ef4dadf680208161c2e80f62c6a73102fe3789f
>>>>>>> bf0cc0cfae67a5b30dc2607068e25e1da5bbc9d0
