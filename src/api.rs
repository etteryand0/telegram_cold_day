pub struct Api {
    token: String,
    admin_id: String,
}

pub trait BotDebug {
    fn traceback(&self, e: String);
}

impl Api {
    pub fn new(token: String, admin_id: String) -> Api {
        Api { token: token, admin_id: admin_id }
    }
}

impl BotDebug for Api {
    fn traceback(&self, e: String) {
        
    }
}