fn factorial(n: u32) -> u32 {
    if n == 0 || n == 1 {
        1
    } else {
        n * factorial(n - 1)
    }
}

fn main() {
    let number = 5;
    println!("Factorial of {} is {}", number, factorial(number));
} 