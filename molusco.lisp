(defun fibonacci (N) 
(if (or (zerop N) (= N 1))
1
(+ (fibonacci (- N 1)) (fibonacci (- N 2)))))

(defun molusco (medida N)
	(if(or (zerop N) (= N 1)) medida
		(molusco (* medida (/ (fibonacci (- N 2)) (fibonacci (- N 1)))) (- N 1))))

trace(molusco)