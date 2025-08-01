fn a1b2c3(x9: u32) -> u32 {
    if x9 == 0 || x9 == 1 {
        1
    } else {
        x9 * a1b2c3(x9 - 1)
    }
}

fn main() {
    let y7 = 5;
    println!("Factorial of {} is {}", y7, a1b2c3(y7));
} 