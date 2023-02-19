(define (split-at lst n)
  (
    cond ((null? (cdr lst)) (cons lst nil))
        ((<= n 0) (cons '() lst))
        (else (cons(cons(car lst) (car (split-at (cdr lst) (- n 1)))) (cdr (split-at (cdr lst) (- n 1)))))
  )
)


(define (compose-all funcs)
  (
    if(null? funcs)

    (lambda (n) n)

    (lambda (n)
    ((compose-all (cdr funcs)) ((car funcs) n)))

  )
)

