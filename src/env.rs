use crate::{ dotenv };

pub fn get_env_variable(key: String) -> String {
    match dotenv::var(&key) {
        Ok(value) => value,
        Err(_) => {
            panic!("{}Файл .env не существует или в нём нет системной переменной {}{}",
                "\x1b[31m", &key, "\x1b[0m"
            );
        }
    }
}