function changeOrder(sort_name, value_1, value_2, default_value) {
    let url = ''
    let cur_url = window.location.href;
    let includes_qm = cur_url.includes('?')
    let includes_sort = cur_url.includes(sort_name);

    if (!includes_sort && !includes_qm) {
        url = cur_url + `?${sort_name}=` + default_value;
    } else if (includes_qm && !includes_sort) {
        url = cur_url + `&${sort_name}=` + default_value;
    } else {
        if (cur_url.includes(`${sort_name}=${value_1}`)) {            
            url = cur_url.replace(`${sort_name}=${value_1}`, `${sort_name}=${value_2}`);
        } else if (cur_url.includes(`${sort_name}=${value_2}`)) {
            url = cur_url.replace(`${sort_name}=${value_2}`, `${sort_name}=${value_1}`);
        }                
    }
    window.location.href = url;
}