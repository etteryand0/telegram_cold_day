use std::time::{Duration, SystemTime};
use std::thread::sleep;

use dotenv;
mod env;
use env::get_env_variable;

fn main() {
    let token = get_env_variable(String::from("TELEGRAM_BOT_TOKEN"));
    let admin = get_env_variable(String::from("TELEGRAM_ADMIN_ID"));

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