def findDecision(obj):
   # Feature: BB, Instances: 115, Entropy: 0.9877
   if obj[3] == 'Sell':
      # Feature: Closing, Instances: 66, Entropy: 0.9894
      if obj[0]>5.626:
         # Feature: RSI, Instances: 62, Entropy: 0.9728
         if obj[1] == 'Hold':
            # Feature: SMA1, Instances: 60, Entropy: 0.9799
            if obj[4] == 'Buy':
               # Feature: MACD, Instances: 34, Entropy: 0.99
               if obj[2] == 'Sell':
                  # Feature: SMA2, Instances: 28, Entropy: 0.9963
                  if obj[5] == 'Buy':
                     return 'No'
                  elif obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 6, Entropy: 0.9183
                  if obj[5] == 'Buy':
                     return 'No'
                  elif obj[5] == 'Sell':
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            elif obj[4] == 'Sell':
               # Feature: MACD, Instances: 26, Entropy: 0.9612
               if obj[2] == 'Buy':
                  # Feature: SMA2, Instances: 15, Entropy: 0.9968
                  if obj[5] == 'Sell':
                     return 'Yes'
                  elif obj[5] == 'Buy':
                     return 'No'
                  else:
                     return 'No'
               elif obj[2] == 'Sell':
                  # Feature: SMA2, Instances: 11, Entropy: 0.8454
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
      elif obj[0]<=5.626:
         return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Hold':
      # Feature: SMA1, Instances: 46, Entropy: 0.7554
      if obj[4] == 'Buy':
         # Feature: MACD, Instances: 35, Entropy: 0.5917
         if obj[2] == 'Buy':
            # Feature: RSI, Instances: 31, Entropy: 0.6374
            if obj[1] == 'Sell':
               # Feature: SMA2, Instances: 16, Entropy: 0.5436
               if obj[5] == 'Buy':
                  # Feature: Closing, Instances: 14, Entropy: 0.5917
                  if obj[0]>5.626:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[1] == 'Hold':
               # Feature: SMA2, Instances: 15, Entropy: 0.7219
               if obj[5] == 'Buy':
                  # Feature: Closing, Instances: 13, Entropy: 0.6194
                  if obj[0]>5.626:
                     return 'Yes'
                  else:
                     return 'Yes'
               elif obj[5] == 'Sell':
                  # Feature: Closing, Instances: 2, Entropy: 1.0
                  if obj[0]>5.626:
                     return 'No'
                  else:
                     return 'No'
               else:
                  return 'No'
            else:
               return 'Yes'
         elif obj[2] == 'Sell':
            return 'Yes'
         else:
            return 'Yes'
      elif obj[4] == 'Sell':
         # Feature: RSI, Instances: 11, Entropy: 0.994
         if obj[1] == 'Hold':
            # Feature: Closing, Instances: 8, Entropy: 0.9544
            if obj[0]>5.626:
               # Feature: SMA2, Instances: 6, Entropy: 0.65
               if obj[5] == 'Buy':
                  return 'No'
               elif obj[5] == 'Sell':
                  return 'Yes'
               else:
                  return 'Yes'
            elif obj[0]<=5.626:
               return 'Yes'
            else:
               return 'Yes'
         elif obj[1] == 'Sell':
            return 'Yes'
         else:
            return 'Yes'
      else:
         return 'Yes'
   elif obj[3] == 'Buy':
      return 'No'
   else:
      return 'No'
