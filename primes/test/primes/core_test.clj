(ns primes.core-test
  (:use clojure.test
        primes.core))

(deftest a-test
  (is (is_prime 1) )
  (is (is_prime 2))
  (is (is_prime 3))
  (is (not (is_prime 4)))
  (is (is_prime 5))
  (is (not (is_prime 6)))
  (is (is_prime 7))
    )

