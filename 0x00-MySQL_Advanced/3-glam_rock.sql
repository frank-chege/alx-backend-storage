--checks for the lifes[an of bands with a style named glam rock.
SELECT band_name,
    (IFNULL(split, '2022') - formed) as lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(style, '')) > 0 
    ORDER BY lifespan DESC;
