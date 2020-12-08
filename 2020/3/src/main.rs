use std::fs;
use anyhow::Result;


fn main() -> Result<()> {
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
        x += 3;
        y += 1;
    }
    println!("{}", trees);
    Ok(())
}
