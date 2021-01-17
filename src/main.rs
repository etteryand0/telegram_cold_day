use std::time::{Duration, SystemTime};
use std::thread::sleep;

use dotenv;

fn main() {
    let token = match dotenv::var("TELEGRAM_BOT_TOKEN") {
        Ok(value) => value,
        Err(_) => {
            panic!("{}Файл .env не существует или в нём нет системной переменной TELEGRAM_BOT_TOKEN{}",
                "\x1b[31m", "\x1b[0m"
            );
        }
    };

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