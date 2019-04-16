.data
	outFormatInt:
	.string "%d\n"
	outFormatStr:
	.string "%s\n"
	inFormat:
	.string "%d\n"
	.global main
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
