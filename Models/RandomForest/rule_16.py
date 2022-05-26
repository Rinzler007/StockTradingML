def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9398
   if obj[3] == 'Sell':
      # Feature: MACD, Instances: 66, Entropy: 0.9993
      if obj[2] == 'Sell':
         # Feature: RSI, Instances: 43, Entropy: 0.9682
         if obj[1] == 'Hold':
            # Feature: Closing, Instances: 41, Entropy: 0.9789
            if obj[0]<=71.11799599999998:
               # Feature: SMA2, Instances: 31, Entropy: 0.9629
               if obj[5] == 'Buy':
                  # Feature: SMA1, Instances: 19, Entropy: 0.9819
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[5] == 'Sell':
                  # Feature: SMA1, Instances: 12, Entropy: 0.9183
                  if obj[4] == 'Buy':
                     return 'No'
                  elif obj[4] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[0]>71.11799599999998:
               # Feature: SMA1, Instances: 10, Entropy: 1.0
               if obj[4] == 'Buy':
                  # Feature: SMA2, Instances: 7, Entropy: 0.9852
                  if obj[5] == 'Buy':
                     return 'No'
                  elif obj[5] == 'Sell':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[4] == 'Sell':
                  # Feature: SMA2, Instances: 3, Entropy: 0.9183
                  if obj[5] == 'Buy':
                     return 'No'
                  elif obj[5] == 'Sell':
                     return 'No'
                  else:
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
         # Feature: Closing, Instances: 23, Entropy: 0.9321
         if obj[0]<=71.11799599999998:
            # Feature: SMA2, Instances: 21, Entropy: 0.9587
            if obj[5] == 'Sell':
               # Feature: SMA1, Instances: 18, Entropy: 0.9183
               if obj[4] == 'Sell':
                  # Feature: RSI, Instances: 16, Entropy: 0.896
                  if obj[1] == 'Hold':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[4] == 'Buy':
                  # Feature: RSI, Instances: 2, Entropy: 1.0
                  if obj[1] == 'Hold':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[5] == 'Buy':
               # Feature: SMA1, Instances: 3, Entropy: 0.9183
               if obj[4] == 'Sell':
                  return 'No'
               elif obj[4] == 'Buy':
                  return 'Yes'
               else:
                  return 'Yes'
            else:
               return 'No'
         elif obj[0]>71.11799599999998:
            return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Hold':
      # Feature: RSI, Instances: 45, Entropy: 0.4328
      if obj[1] == 'Hold':
         # Feature: SMA1, Instances: 23, Entropy: 0.6666
         if obj[4] == 'Buy':
            # Feature: Closing, Instances: 15, Entropy: 0.3534
            if obj[0]<=71.11799599999998:
               # Feature: MACD, Instances: 9, Entropy: 0.5033
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 7, Entropy: 0.5917
                  if obj[5] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[2] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[0]>71.11799599999998:
               return 'Yes'
            else:
               return 'Yes'
         elif obj[4] == 'Sell':
            # Feature: SMA2, Instances: 8, Entropy: 0.9544
            if obj[5] == 'Buy':
               # Feature: Closing, Instances: 7, Entropy: 0.9852
               if obj[0]<=71.11799599999998:
                  # Feature: MACD, Instances: 4, Entropy: 1.0
                  if obj[2] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[0]>71.11799599999998:
                  # Feature: MACD, Instances: 3, Entropy: 0.9183
                  if obj[2] == 'Buy':
                     return 'Yes'
                  else:
                     return 'Yes'
               else:
                  return 'Yes'
            elif obj[5] == 'Sell':
               return 'Yes'
            else:
               return 'Yes'
         else:
            return 'Yes'
      elif obj[1] == 'Sell':
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      # Feature: MACD, Instances: 4, Entropy: 0.8113
      if obj[2] == 'Sell':
         return 'No'
      elif obj[2] == 'Buy':
         return 'Yes'
      else:
         return 'Yes'
   else:
      return 'No'
