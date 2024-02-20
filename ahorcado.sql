CREATE TABLE usuarios (
    usuario VARCHAR(50) PRIMARY KEY,
    contrasena_hash VARCHAR(255) NOT NULL
);

CREATE TABLE intentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50),
    palabra VARCHAR(50),
    n_fallos INT,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	FOREIGN KEY (usuario) REFERENCES usuarios(usuario) ON DELETE CASCADE
)ENGINE=INNODB;

CREATE TABLE palabras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    palabra VARCHAR(255) NOT NULL,
    usuario VARCHAR(255) NOT NULL,
    fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)ENGINE=INNODB;

select * from intentos;
select * from usuarios;
select * from palabras;