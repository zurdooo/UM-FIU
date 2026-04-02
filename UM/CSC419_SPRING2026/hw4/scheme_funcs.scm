; Exercise C

(define (count-ones lis)
  (cond
    ((null? lis) 0)                         
    ((= (car lis) 1)                        
     (+ 1 (count-ones (cdr lis))))         
    (else
     (count-ones (cdr lis)))))             




; Exercise D

(define (count-ones-nested lis)
  (cond
    ((null? lis) 0)                       

    ((not (list? (car lis)))
     (if (= (car lis) 1)
         (+ 1 (count-ones-nested (cdr lis))) 
         (count-ones-nested (cdr lis))))    


    (else
     (+ (count-ones-nested (car lis))        
        (count-ones-nested (cdr lis))))))    

; Exercise E

(define (cube-list lis)
  (map (lambda (x) (* x x x)) lis))      

