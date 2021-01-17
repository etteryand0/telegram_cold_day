use std::time::{Duration, SystemTime};
use std::thread::sleep;

fn main() {
    while true {
        let now = SystemTime::now();

        sleep(Duration::new(10, 0));
        match now.elapsed() {
            Ok(elapsed) => {
                println!("Elapsed {} seconds", elapsed.as_secs());
            }
            Err(e) => {
                println!("Error: {:?}", e);
                break;
            }
        }
    }
    println!("Script stopped");
}