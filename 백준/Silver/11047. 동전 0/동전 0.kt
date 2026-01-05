// 일단 빠른 입력에서 계속 컴파일 에러가 나니깐 기본 입력으로 받아보자
// K원을 만들기 위해서 N 종류의 동전을 최소한의 개수만 사용하는 게 목표다

// 내가 보기엔 K원보다 작은 종류 중 가장 큰 값만을 사용하면 될 것으로 보인다.
// 입력을 받을 때 K보다 큰 동전을 애초에 저장하지 말고, 나머지 값만 활용하면 빠르지 않을까?
// 왜나면 오름차순으로 주어지니깐!

import java.util.Scanner

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
    // 1. N, K 입력 받기
    val N = nextInt()
    val K = nextInt()

    // 2. K보다 작은 값만 배열에 집어 넣기
    var A = intArrayOf(N)

    for (i: Int in 0..< N) {
        val nextValue = nextInt()

        if (nextValue > K) {
            break
        }

        A = A.plus(nextValue)
    }

    // 3. remain 0 만들기 전까지 반복
    var remain: Int = K
    var result = 0
    for (a in A.reversed()) {
        if (remain == 0) {
            break
        }
        val div = remain / a
        remain %= a
        result += div
    }

    println(result)
}