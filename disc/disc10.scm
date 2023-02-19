(define (factorial x)
        (if (= x 0) 1 (* x (factorial (- x 1))))
)

(define (fib n)
    (
        cond
            ((= n 0) 0)
            ((= n 1) 1)
            (else (+ fib(- n 1) fib(- n 2)))
    )
)

(define (my-append a b)
    (
        cond
            ((eq? a '()) b)
            ((eq? b '()) a)
            (else (cons (car a) (my-append (cdr a) b)))

    )
)

(define (find_three s)
    (
        cond
            ((eq? s '()) #f)
            ((list? (car s)) (or (find_three(car s)) (find_three(cdr s))))
            ((= (car s) 3) #t)
            (else (find_three(cdr s)))
    )
)

(define (duplicate lst)
    (if (eq? lst '())
         '()
        (cons (car lst) (cons (car lst) (duplicate(cdr lst))))
    )
)

(define (insert element lst index)
    (if (= index 0)
        (cons element lst)
        (cons (car lst) (insert element (cdr lst) (- index 1)))
    )
)