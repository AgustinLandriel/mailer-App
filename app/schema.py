instructions = [
    'DROP TABLE IF EXISTS EMAIL;',
    """
        CREATE TABLE email (
            id INT PRIMARY KEY AUTO_INCREMENT,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """
]