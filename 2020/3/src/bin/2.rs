use std::fs;
use anyhow::Result;


fn run_slope(x_add: usize, y_add: usize) -> Result<usize> {
    let text = fs::read_to_string("input")?;
    let input: Vec<&str> = text.lines().collect();
    let y_len = input.len();
    let x_len = input[0].len();
    let mut trees = 0;
    let mut x = 0;
    let mut y = 0;
    while y < y_len {
        if input[y].chars().nth(x % x_len) == Some('#') {
            trees += 1;
        }
        x += x_add;
        y += y_add;
    }
    Ok(trees)

}

fn main() -> Result<()> {
    println!("{}", run_slope(1, 1)? * run_slope(3, 1)? * run_slope(5, 1)? * run_slope(7, 1)? * run_slope(1, 2)?);
    Ok(())
}
