from time import gmtime, strftime, time

# below, using -d instead of just d to have only one number for day
# -> '1' instead of '01'
epok = strftime("%B %-d, %Y:", gmtime(0))
elapsed_seconds = int(time())
current_time = strftime("%b %d %Y", gmtime())
print("Seconds since", epok, "{:,}".format(elapsed_seconds), "or",
      f"{elapsed_seconds:.2e}", "in scientific notation")
print(current_time)  # print current_time separately to avoid leading space
