create table Etablissement
      (
          UAI                                   VARCHAR(32) not null
              primary key
              unique,
          SIRET                                 DOUBLE      null,
          type                                  TEXT        null,
          nom                                   TEXT        null,
          sigle                                 TEXT        null,
          statut                                TEXT        null,
          tutelle                               TEXT        null,
          universiteDeRattachementLibelle       TEXT        null,
          universiteDeRattachementIDetURLOnisep TEXT        null,
          etablissementsLiesLibelles            TEXT        null,
          etablissementsLiesURLetIDOnisep       TEXT        null,
          boitePostale                          TEXT        null,
          adresse                               TEXT        null,
          codePostal                            INT         null,
          commune                               TEXT        null,
          numcommune                            TEXT        null,
          cedex                                 TEXT        null,
          telephone                             int         null,
          arrondissement                        INT         null,
          departement                           TEXT        null,
          academie                              TEXT        null,
          region                                TEXT        null,
          numRegion                             INT         null,
          longitude                             DOUBLE      null,
          latitude                              DOUBLE      null,
          journeesportesouvertes                TEXT        null,
          labelGeneration2024                   TEXT        null,
          URLetIDOnisep                         TEXT        null
      )

ALTER TABLE Etablissement DROP COLUMN cedex;
ALTER TABLE Etablissement DROP COLUMN numcommune;
ALTER TABLE Etablissement DROP COLUMN journeesportesouvertes;
ALTER TABLE Etablissement DROP COLUMN arrondissement;

# DONE Supprimer Etablissement sans UAI
delete from Etablissement where UAI=' ' OR UAI IS NULL;
alter table Etablissement
    modify UAI text not null;
alter table Etablissement
    modify UAI VARCHAR(32) not null;

# DONE Rajouter ID pour Etablissement
ALTER TABLE Etablissement ADD id MEDIUMINT NOT NULL AUTO_INCREMENT KEY;
alter table Etablissement drop primary key, add constraint primary key (id);

# DONE créer une table organisme de tutelle et rajouter une clé etrangère dans Etablissement

create table organisme_tutelle(
    nom_organisme           TEXT
);
insert into organisme_tutelle (nom_organisme)
    select distinct tutelle from Etablissement where tutelle is not null;
alter table organisme_tutelle
    modify nom_organisme VARCHAR(128) null;
ALTER TABLE organisme_tutelle ADD id int NOT NULL AUTO_INCREMENT KEY;

UPDATE Etablissement E
JOIN organisme_tutelle O ON E.tutelle = O.nom_organisme
set E.tutelle = O.id;

alter table Etablissement
    RENAME COLUMN tutelle to id_tutelle;

alter table Etablissement
    modify id_tutelle int;

alter table Etablissement
    add constraint foreign key (id_tutelle) references organisme_tutelle(id);


# TODO créer une table organisme de université de rattachement et rajouter une clé etrangère dans Etablissement
# TODO etablissmeent lié libelé en clé etrangeree
# TODO table académie
# TODO transformer generaction24 en boolean
# TODO clean CFA et Etablissement
# TODO changer des colonnes en Enum