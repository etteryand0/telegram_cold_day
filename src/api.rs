pub struct Api {
    token: String,
    admin_id: String,
}

impl Api {
    pub fn new(token: String, admin_id: String) -> Api {
        Api { token: token, admin_id: admin_id }
    }
}