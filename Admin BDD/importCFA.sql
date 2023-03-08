create table CFA
(
    numero_convention               VARCHAR(32) not null
        primary key
        unique,
    nom                             TEXT   null,
    adresse                         TEXT   null,
    complement_adresse              TEXT   null,
    dpt                             INT    null,
    code_postal                     INT    null,
    commune                         TEXT   null,
    date_debut_convention           DATE   null,
    date_fin_convention             DATE   null,
    nom_cfa_conventionnel           TEXT   null,
    nom_court_cfa_conventionnel     TEXT   null,
    adresse_cfa_conventionnel       TEXT   null,
    adresse_cfa_conventionnel_suite TEXT   null,
    code_postal_cfa_conventionnel   INT    null,
    ville_cfa_conventionnel         TEXT   null,
    lat                             DOUBLE null,
    lng                             DOUBLE null,
    wgs84                           TEXT   null
)
    comment 'table regroupant les CFA';

ALTER TABLE CFA DROP COLUMN dpt;
ALTER TABLE CFA DROP COLUMN nom_cfa_conventionnel;
ALTER TABLE CFA DROP COLUMN adresse_cfa_conventionnel;
ALTER TABLE CFA DROP COLUMN adresse_cfa_conventionnel_suite;
ALTER TABLE CFA DROP COLUMN wgs84;