CREATE TABLE if NOT EXISTS users (
    UserId text PRIMARY KEY,
    UserName text,
    MessagesSent INTEGER DEFAULT 0,
    Coins INTEGER DEFAULT 0,
    CoinLock text DEFAULT CURRENT_TIMESTAMP,
    Warnings INTEGER DEFAULT 0

);
