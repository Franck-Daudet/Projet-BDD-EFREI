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