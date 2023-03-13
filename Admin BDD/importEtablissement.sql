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
# TODO Supprimer Etablissement sans UAI
# TODO Rajouter ID pour Etablissement
# TODO créer une table organisme de tutelle et rajouter une clé etrangère dans Etablissement
# TODO créer une table organisme de université de rattachement et rajouter une clé etrangère dans Etablissement
# TODO etablissmeent lié libelé en clé etrangeree
# TODO table académie
# TODO transformer generaction24 en boolean
# TODO clean CFA et Etablissement
# TODO changer des colonnes en Enum