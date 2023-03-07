create table credit
      (
          nom    varchar(32) not null,
          prenom varchar(32) null,
          age    int         null
      );

INSERT INTO Main.Credit (nom, prenom, age)
VALUES ('DAUDET', 'Franck', 21);

INSERT INTO Main.Credit (nom, prenom, age)
VALUES ('ANDRIANARIJAONA', 'Andy', 20);

INSERT INTO Main.Credit (nom, prenom, age)
VALUES ('AMEZIANE', 'Ines', 21);

INSERT INTO Main.Credit (nom, prenom, age)
VALUES ('BRIENT', 'Manon', 20);
