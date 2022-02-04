# Taiwan Art & Culture Open Data Data Preprocess

## General Info

This project can help you get the Art and Cultural Activities information from open data website. Including basic 15 art and cultural activities at below.

1. 音樂
2. 戲劇
3. 舞蹈
4. 親子
5. 獨立音樂
6. 展覽
7. 講座
8. 電影
9. 綜藝
10. 競賽
11. 徵選
12. 其他
13. 內部資料
14. 演唱會
15. 研習課程

## Setup

1. First of all, you have to create a Database and named it  “Activity”.
2. Run `dbScript.sql` code, it would create some relation tables.
    1. activityInfo
    2. city
    3. showInfo
3. And now your city table is empty, so we have to insert some Taiwan city information to this table. Run the code below.
    
    ```sql
    insert into city
                values (N'臺北市', 1),
                (N'台北市', 1),
                (N'新北市', 2),
                (N'桃園市', 3),
                (N'臺中市', 4),
                (N'台中市', 4),
                (N'臺南市', 5),
                (N'台南市', 5),
                (N'高雄市', 6),
                (N'新竹縣', 7),
                (N'苗栗縣', 8),
                (N'彰化縣', 9),
                (N'南投縣', 10),
                (N'雲林縣', 11),
                (N'嘉義縣', 12),
                (N'屏東縣', 13),
                (N'宜蘭縣', 14),
                (N'花蓮縣', 15),
                (N'臺東縣', 16),
                (N'澎湖縣', 17),
                (N'金門縣', 18),
                (N'連江縣', 19),
                (N'基隆縣', 20),
                (N'新竹市', 21),
                (N'嘉義市', 22),
                (N'未知', 23);
    ```
    
4. Run [activity.py](http://activity.py) file and the art and cultural information will insert into table automatically.

## Some Auxiliary SQL code

1. The proportion of arts and cultural activities in each city.
    
    ```sql
    select YEAR(a.time) as year, city.city, count(*) as count
    	from (
      select showInfo.time, city.cityIndex
      from [Activity].[dbo].[showInfo]
      left join city on showInfo.location like CONCAT('%', city.city, '%')
      left join activityInfo on showInfo.UID = activityInfo.UID
      ) as a
      join city on a.cityIndex=city.cityIndex
      where city.city not like '%台%'
      group by YEAR(a.time), city.city
      order by YEAR(a.time), count(*) desc
    ```
    
2. The proportion of activities in each city of each year.
    
    ```sql
    select city.city, a.category, count(*) as count
    	from (
      select showInfo.time, city.cityIndex, activityInfo.category
      from [Activity].[dbo].[showInfo]
      left join city on showInfo.location like CONCAT('%', city.city, '%')
      left join activityInfo on showInfo.UID = activityInfo.UID
      ) as a
      join city on a.cityIndex = city.cityIndex
      where city.city not like '%台%'
      group by city.city, a.category
      order by city.city asc, count(*) desc
    ```
    
3. CTR for each category.
    
    ```sql
    select category, count(activityInfo.hitRate) as count
      from [Activity].[dbo].activityInfo
      group by category
      order by category asc
    ```
