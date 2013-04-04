(ns primes.core)

(defn is_prime [ n ] 
	(cond  
		(or (= n 0) (= n 1) (= n 2))  true
		(= (filter (fn [ iter_n ] (= (mod n iter_n) 0)) 
		(range 2 (+ (/ n 2) 1))) ()) true	
		false false
	))	
	
(defn -main
  "I don't do a whole lot."
  [& args]
  (println "Hello, World!"))
