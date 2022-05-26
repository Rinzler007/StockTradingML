def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9986
   if obj[3] == 'Sell':
      # Feature: Closing, Instances: 73, Entropy: 0.9693
      if obj[0]<=52.034:
         # Feature: RSI, Instances: 40, Entropy: 0.9982
         if obj[1] == 'Hold':
            # Feature: SMA2, Instances: 39, Entropy: 0.9957
            if obj[5] == 'Buy':
               # Feature: SMA1, Instances: 23, Entropy: 0.9877
               if obj[4] == 'Buy':
                  # Feature: MACD, Instances: 19, Entropy: 0.9819
                  if obj[2] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[4] == 'Sell':
                  # Feature: MACD, Instances: 4, Entropy: 1.0
                  if obj[2] == 'Sell':
                     return 'No'
                  elif obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Sell':
               # Feature: MACD, Instances: 16, Entropy: 1.0
               if obj[2] == 'Sell':
                  # Feature: SMA1, Instances: 9, Entropy: 0.9911
                  if obj[4] == 'Buy':
                     return 'Yes'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Buy':
                  # Feature: SMA1, Instances: 7, Entropy: 0.9852
                  if obj[4] == 'Sell':
                     return 'Yes'
                  elif obj[4] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         elif obj[1] == 'Buy':
            return 'Yes'
         else:
            return 'Yes'
      elif obj[0]>52.034:
         # Feature: MACD, Instances: 33, Entropy: 0.885
         if obj[2] == 'Sell':
            # Feature: RSI, Instances: 20, Entropy: 0.7219
            if obj[1] == 'Hold':
               # Feature: SMA2, Instances: 18, Entropy: 0.7642
               if obj[5] == 'Buy':
                  # Feature: SMA1, Instances: 11, Entropy: 0.8454
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  # Feature: SMA1, Instances: 7, Entropy: 0.5917
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[1] == 'Buy':
               return 'No'
            else:
               return 'No'
         elif obj[2] == 'Buy':
            # Feature: SMA1, Instances: 13, Entropy: 0.9957
            if obj[4] == 'Sell':
               # Feature: RSI, Instances: 7, Entropy: 0.8631
               if obj[1] == 'Hold':
                  # Feature: SMA2, Instances: 7, Entropy: 0.8631
                  if obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Buy':
               # Feature: SMA2, Instances: 6, Entropy: 0.9183
               if obj[5] == 'Sell':
                  # Feature: RSI, Instances: 5, Entropy: 0.971
                  if obj[1] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Buy':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         else:
            return 'No'
      else:
         return 'No'
   elif obj[3] == 'Hold':
      # Feature: SMA1, Instances: 39, Entropy: 0.7321
      if obj[4] == 'Buy':
         # Feature: Closing, Instances: 21, Entropy: 0.2762
         if obj[0]<=52.034:
            return 'Yes'
         elif obj[0]>52.034:
            # Feature: RSI, Instances: 9, Entropy: 0.5033
            if obj[1] == 'Hold':
               # Feature: MACD, Instances: 5, Entropy: 0.7219
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 3, Entropy: 0.9183
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[1] == 'Sell':
               return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[4] == 'Sell':
         # Feature: Closing, Instances: 18, Entropy: 0.9641
         if obj[0]<=52.034:
            # Feature: RSI, Instances: 11, Entropy: 0.684
            if obj[1] == 'Sell':
               return 'Yes'
            elif obj[1] == 'Hold':
               # Feature: SMA2, Instances: 5, Entropy: 0.971
               if obj[5] == 'Buy':
                  # Feature: MACD, Instances: 3, Entropy: 0.9183
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'Yes'
         elif obj[0]>52.034:
            # Feature: SMA2, Instances: 7, Entropy: 0.8631
            if obj[5] == 'Buy':
               # Feature: RSI, Instances: 5, Entropy: 0.7219
               if obj[1] == 'Hold':
                  # Feature: MACD, Instances: 3, Entropy: 0.9183
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[1] == 'Sell':
                  return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Sell':
               # Feature: RSI, Instances: 2, Entropy: 1.0
               if obj[1] == 'Sell':
                  return 'Yes'
               elif obj[1] == 'Hold':
                  return 'No'
               else:
                  return 'No'
            else:
               return 'No'
         else:
            return 'No'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      return 'No'
   else:
      return 'No'
