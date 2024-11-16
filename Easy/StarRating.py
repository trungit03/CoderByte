def StarRating(str):
    convert_str = float(str)
    round_str = round(convert_str * 2)
    full_stars = round_str // 2
    half_stars = round_str % 2 != 0
    empty = 5 - full_stars - half_stars
    images_name = ['full']*full_stars
    if half_stars:
        images_name.append('half')
    images_name.extend(['empty']*empty)

    return ' '.join(images_name)

print(StarRating(0.1))
print(StarRating(0.38))
print(StarRating(2.0))
print(StarRating(2.5))