

void PyInit_caldistance()
{
    return;
}

float CalDistance(float lat1, float lat2, float longti1, float longti2)
{
    float pi_num = 0.01745329 ;
    float earth = 6378137 ;
    float radlat1 = lat1 * pi_num ;
    float radlat2 = lat2 * pi_num ;
    float radlongti1 = longti1 * pi_num ;
    float radlongti2 = longti2 * pi_num ;
    float a = radlat1 - radlat2 ;
    float b = radlongti1 - radlongti2 ;
    float temp_a = pow(sin(a/2), 2) ;
    float temp_b_sin = pow(sin(b/2), 2) ;
    float temp_b = cos(radlat1) * cos(radlat2) * temp_b_sin ;
    float temp_asin = sqrt(temp_a+temp_b) ;
    float s = asin(temp_asin) ;
    float result = fabs(s*earth) ;
    return result;
}