function clearSorts() {
    let url = '';
    let cur_url = window.location.href;
    index_of_qm = cur_url.indexOf('?')
    if (index_of_qm != -1) {
        url = cur_url.slice(0, index_of_qm)
        window.location.href = url;
    }
}