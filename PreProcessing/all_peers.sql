 
 CREATE or replace EXTERNAL TABLE `wpn-gigi.chatgpt.ext_peer16`
(
  idea STRING,
  rel STRING,
  inn STRING,
  ins STRING,
  empty STRING,
  idea2 STRING,
  rel2 STRING,
  inn2 STRING,
  ins2 STRING
)
OPTIONS(
  sheet_range="Team 6!A7:I33",
  format="GOOGLE_SHEETS",
  uris=["https://docs.google.com/spreadsheets/d/1WfqlNCSiwHbJPrCfggVbgWry7Nfg6Nr21PRvQx9188M/edit#gid=0"]
); 

CREATE or replace EXTERNAL TABLE `wpn-gigi.chatgpt.ext_peer26`
(
  idea STRING,
  rel STRING,
  inn STRING,
  ins STRING,
  empty STRING,
  idea2 STRING,
  rel2 STRING,
  inn2 STRING,
  ins2 STRING
)
OPTIONS(
  sheet_range="Team 6!A7:I33",
  format="GOOGLE_SHEETS",
  uris=["https://docs.google.com/spreadsheets/d/1fbcl_A2O0NMVNZ42MhigOiM5hOZ9NcVOtGtW_dlgma8/edit#gid=0"]
); 
CREATE or replace EXTERNAL TABLE `wpn-gigi.chatgpt.ext_peer36`
(
  idea STRING,
  rel STRING,
  inn STRING,
  ins STRING,
  empty STRING,
  idea2 STRING,
  rel2 STRING,
  inn2 STRING,
  ins2 STRING
)
OPTIONS(
  sheet_range="Team 6!A7:I33",
  format="GOOGLE_SHEETS",
  uris=["https://docs.google.com/spreadsheets/d/1-cqblpdRHYHQcdgGLOH_4pw3_WtxUSrOAEvvvJ4qRWI/edit#gid=0"]
); 
 CREATE or replace EXTERNAL TABLE `wpn-gigi.chatgpt.ext_peer46` 
(
  idea STRING,
  rel STRING,
  inn STRING,
  ins STRING,
  empty STRING,
  idea2 STRING,
  rel2 STRING,
  inn2 STRING,
  ins2 STRING
)
OPTIONS(
  sheet_range="Team 6!A7:I33",
  format="GOOGLE_SHEETS",
  uris=["https://docs.google.com/spreadsheets/d/1AIuNBFcDaKHrfUBOIZ1gEMBkTwce-_QmGFpGR2s1irk/edit#gid=0"]
); 
 CREATE or replace EXTERNAL TABLE `wpn-gigi.chatgpt.ext_peer56`
(
  idea STRING,
  rel STRING,
  inn STRING,
  ins STRING,
  empty STRING,
  idea2 STRING,
  rel2 STRING,
  inn2 STRING,
  ins2 STRING
)
OPTIONS(
  sheet_range="Team 6!A7:I33",
  format="GOOGLE_SHEETS",
  uris=["https://docs.google.com/spreadsheets/d/1pIzbDm9La8ES7FWpvvAuPxCEI5mO0bOZmqtZU6jDcdo/edit#gid=0"]
); 
 CREATE or replace EXTERNAL TABLE `wpn-gigi.chatgpt.ext_peer66`
(
  idea STRING,
  rel STRING,
  inn STRING,
  ins STRING,
  empty STRING,
  idea2 STRING,
  rel2 STRING,
  inn2 STRING,
  ins2 STRING
)
OPTIONS(
  sheet_range="Team 6!A7:I33",
  format="GOOGLE_SHEETS",
  uris=["https://docs.google.com/spreadsheets/d/1V1m9f9GfUaYZFauqWZO-ND2DiCZyWFmfEh0XgwaO-mE/edit#gid=0"]
); 



with all_peers as 
(
SELECT 1 team ,1 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer11`       union all 
SELECT 1 team ,1 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer11`   union all 
SELECT 1 team ,2 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer21`       union all 
SELECT 1 team ,2 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer21`   union all 
SELECT 1 team ,3 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer31`       union all 
SELECT 1 team ,3 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer31`   union all 
SELECT 1 team ,4 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer41`       union all 
SELECT 1 team ,4 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer41`   union all 
SELECT 1 team ,5 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer51`       union all 
SELECT 1 team ,5 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer51`   union all 
SELECT 1 team ,6 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer61`       union all 
SELECT 1 team ,6 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer61`   
--
union all
--
SELECT 2 team ,1 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer12`       union all 
SELECT 2 team ,1 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer12`   union all 
SELECT 2 team ,2 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer22`       union all 
SELECT 2 team ,2 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer22`   union all 
SELECT 2 team ,3 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer32`       union all 
SELECT 2 team ,3 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer32`   union all 
SELECT 2 team ,4 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer42`       union all 
SELECT 2 team ,4 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer42`   union all 
SELECT 2 team ,5 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer52`       union all 
SELECT 2 team ,5 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer52`   union all 
SELECT 2 team ,6 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer62`       union all 
SELECT 2 team ,6 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer62` 
--
union all
--
SELECT 3 team ,1 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer13`       union all 
SELECT 3 team ,1 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer13`   union all 
SELECT 3 team ,2 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer23`       union all 
SELECT 3 team ,2 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer23`   union all 
SELECT 3 team ,3 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer33`       union all 
SELECT 3 team ,3 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer33`   union all 
SELECT 3 team ,4 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer43`       union all 
SELECT 3 team ,4 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer43`   union all 
SELECT 3 team ,5 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer53`       union all 
SELECT 3 team ,5 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer53`   union all 
SELECT 3 team ,6 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer63`       union all 
SELECT 3 team ,6 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer63` 
--
union all
--
SELECT 4 team ,1 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer14`       union all 
SELECT 4 team ,1 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer14`   union all 
SELECT 4 team ,2 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer24`       union all 
SELECT 4 team ,2 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer24`   union all 
SELECT 4 team ,3 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer34`       union all 
SELECT 4 team ,3 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer34`   union all 
SELECT 4 team ,4 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer44`       union all 
SELECT 4 team ,4 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer44`   union all 
SELECT 4 team ,5 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer54`       union all 
SELECT 4 team ,5 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer54`   union all 
SELECT 4 team ,6 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer64`       union all 
SELECT 4 team ,6 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer64`   
--
union all
--
SELECT 5 team ,1 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer15`       union all 
SELECT 5 team ,1 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer15`   union all 
SELECT 5 team ,2 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer25`       union all 
SELECT 5 team ,2 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer25`   union all 
SELECT 5 team ,3 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer35`       union all 
SELECT 5 team ,3 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer35`   union all 
SELECT 5 team ,4 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer45`       union all 
SELECT 5 team ,4 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer45`   union all 
SELECT 5 team ,5 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer55`       union all 
SELECT 5 team ,5 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer55`   union all 
SELECT 5 team ,6 peer , 1 sett , idea,rel,inn,ins  FROM `wpn-gigi.chatgpt.ext_peer65`       union all 
SELECT 5 team ,6 peer , 2 sett , idea2,rel2,inn2,ins2  FROM `wpn-gigi.chatgpt.ext_peer65` 
 
 
) 
select 'novice' rator , peer,sett , lower(idea) idea_l , left ( lower(idea),45) idea45 , left (rel,1) rel , left(inn,1) inn , left (ins,1) ins  from all_peers  where idea not like 'Idea Set%' and  idea is not null 