pub fn main() {
    let mut a: [i32; 2] = [1, 2];
    let b: [i32; 3] = [1, 2, 3];
    a.copy_from_slice(&b);
}