const OPTIONS_DATE_FORMAT = {
  year: "numeric",
  month: "numeric",
  day: "numeric",
  hour: "numeric",
  minute: "numeric",
  hour12: false,
};

export default {
  parseDate: function(date) {
    const dateUtc = new Date(date);
    return new Intl.DateTimeFormat("en-US", OPTIONS_DATE_FORMAT).format(dateUtc);
  }
};
